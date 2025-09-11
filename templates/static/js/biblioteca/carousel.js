function showHtml (books) {
  const subContainer = document.querySelector('.subcontainer');
  subContainer.classList.add('loading');

  window.addEventListener('load',function(){
    subContainer.classList.remove('loading');
  });

  const baseUrl = "http://localhost:8001/media";
  const cardTemplate = document.querySelector('[data-card-template]');

  /*
  const books = [
    [0, "wilder-girls.jpeg","Wilder Chica","Rory Power","Drama"] ,
    [1,"the-between.jpeg","The Between","David Hofmeyr","Fiction"],
    [2,"our-italian-summer.jpeg","Our Italian Summer","Jennifer Probst","Romance"],
    [3,"little-life.jpeg", "A Little Life","Yanagihara","Biography"],
    [4,"great-miracle.jpeg","Great Miracle","Maggie Shipsted","Fiction"],
    [5,"all-the-bright-places.jpeg","All the Bright Places","Jennifer Niven","Romance"],
    [6,"girl-in-the-translation.jpeg","Girl in Translation","Jean Kwok","Drama"],
    [7,"big-little-lies.jpeg","Big Little Lies","Liane Moriarty","Thriller"],
    [8,"arrival.jpeg","Arrival","Ted Chiang","Fantasy"],
    [9,"moral-compass.jpeg","Moral Compass","Danielle Steel","Fiction"],
    [10,"luck-of-the-titanic.jpeg","Luck of the Titanic","Stacey Lee","Drama"],
    [11,"the-disappearing-act.jpeg","Disappearing Act","Catherine","Thriller"]
  ]
  */

  books.forEach((book)=>{
    const card = document.importNode(cardTemplate.content,true);
    card.querySelector('img').id = book.id;
    card.querySelector('img').src=`${baseUrl+book.file}`; 
    card.querySelector('[data-title]').textContent = book.name;
    card.querySelector('[data-genre]').textContent = book.estado;
    card.querySelector('[data-author]').textContent = book.created_by;
    subContainer.appendChild(card);   
  });
};
