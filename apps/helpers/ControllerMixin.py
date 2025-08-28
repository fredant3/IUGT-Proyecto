import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import error
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import HttpResponseRedirect, JsonResponse, QueryDict
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView


class ListController(LoginRequiredMixin, ListView):
    def get_queryset(self):
        draw = int(self.request.GET.get("draw")) if self.request.GET.get("draw") else 1
        start = (
            int(self.request.GET.get("start")) if self.request.GET.get("start") else 0
        )
        length = (
            int(self.request.GET.get("length"))
            if self.request.GET.get("length")
            else 10
        )
        search = self.request.GET.get("search[value]") or None

        columns = []
        i = 0
        while True:
            searchable = self.request.GET.get(f"columns[{i}][searchable]")
            if searchable is False or searchable == "false" or searchable is None:
                break

            col_name = self.request.GET.get(f"columns[{i}][name]")
            if not col_name:
                break

            col_search = self.request.GET.get(f"columns[{i}][search][value]")
            if col_search:
                columns.append({"name": col_name, "search": col_search})

            i += 1

        orderBy = self.request.GET.get("order[0][name]") or None
        orderAsc = self.request.GET.get("order[0][dir]") or None

        return self.service.getAll(
            draw, start, length, search, orderBy, orderAsc, (""), columns
        )

    def get(self, request, *args, **kwargs):
        data = {}
        try:
            data = self.get_queryset()
        except Exception as e:
            data["error"] = str(e)
        return JsonResponse(data, safe=False)

    class Meta:
        abstract = True


class CreateController(LoginRequiredMixin, CreateView):
    def post(self, request, *arg, **kwargs):
        if (
            request.method == "POST"
            and request.headers.get("X-Requested-With") == "XMLHttpRequest"
        ):
            try:
                self.service.creator(self.get_form(), request, *arg, **kwargs)
                return JsonResponse({"message": "Se ha registrado con éxito."})
            except ValidationError as e:
                try:
                    return JsonResponse(
                        {
                            "errors": (
                                json.loads(e.message.replace("'", '"'))
                                if isinstance(e.message, str)
                                else e.message
                            )
                        }
                    )
                except Exception:
                    return JsonResponse(
                        {
                            "errors": (
                                json.loads(e.message)
                                if isinstance(e.message, str)
                                else e.message
                            )
                        }
                    )

    class Meta:
        abstract = True


class UpdateController(LoginRequiredMixin, UpdateView):
    http_method_names = ["get", "post", "put"]
    redirect_not_found = None

    def get_url_redirect(self):
        if self.redirect_not_found is None:
            return reverse_lazy("auth:login")
        return self.redirect_not_found

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Exception:
            return HttpResponseRedirect(self.get_url_redirect())

        if self.request.method.upper() == "PUT":
            return self.put(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user.username
                return data
            except ObjectDoesNotExist:
                error(self.request, "El recurso no se ha encontrado")
        else:
            error(self.request, "No se proporcionó ningún recurso válido")

    def get_form(self):
        return self.form_class(
            QueryDict(self.request.body) or None, instance=self.get_object()
        )

    def put(self, request, *arg, **kwargs):
        if self.request.headers.get("x-requested-with") == "XMLHttpRequest":
            try:
                self.service.updater(self.get_object(), self.get_form())
                return JsonResponse({"message": "Se ha actualizado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

    class Meta:
        abstract = True


class DeleteController(LoginRequiredMixin, DeleteView):
    redirect_not_found = None

    def get_url_redirect(self):
        if self.redirect_not_found is None:
            return reverse_lazy("auth:login")
        return self.redirect_not_found

    def dispatch(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Exception:
            return HttpResponseRedirect(self.get_url_redirect())

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, **kwargs):
        pk = self.kwargs.get("pk")

        if pk:
            try:
                data = self.service.reader(pk)
                data.updated_by = self.request.user.username
                data.deleted_by = self.request.user.username
                return data
            except ObjectDoesNotExist:
                error(self.request, "El recurso no se ha encontrado")
        else:
            error(self.request, "No se proporcionó ningún recurso válido")

    def delete(self, request, pk, *arg, **kwargs):
        if (
            request.method == "DELETE"
            and request.headers.get("x-requested-with") == "XMLHttpRequest"
        ):
            try:
                self.service.destroyer(self.get_object())
                return JsonResponse({"message": "Se ha eliminado con éxito."})
            except ValidationError as e:
                return JsonResponse({"errors": json.loads(e.message)})

    class Meta:
        abstract = True
