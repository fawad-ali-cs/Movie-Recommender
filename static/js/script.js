var item_num = 1;
const item_num_list = [];

const liked_movies = [];

function myFunction() {
  	var title = document.getElementById('usr').value;

  	if (data.includes(title) & !liked_movies.includes(title)) {
  		liked_movies.push(title);
  		item_num_list.push("item" + item_num);

	  	var ul = document.getElementById("favorite-list");
	  	var li = document.createElement("li");

	  	var remove_button = document.createElement("button");
	  	remove_button.setAttribute("class", "btn btn-danger btn-xs");
	  	remove_button.innerHTML = "X";

	  	remove_button.setAttribute("onclick","remove_item(this)"); 
		remove_button.setAttribute("id","item" + item_num);
		li.setAttribute("id","item" + item_num);

		max_length = 30

		if (title.length >= max_length) {
			title = title.slice(0,max_length-10) + "..." + title.slice(title.length - 6 ,title.length)
		}

		item_num += 1;
	  	var space_count = max_length - title.length
	  	var space = "&nbsp;";

	  	li.innerHTML = title + space.repeat(space_count);
	  	li.appendChild(remove_button);

	  	ul.appendChild(li);
	  	
	  	document.getElementById('usr').value = "";
	}
}

function remove_item(element) {
	movie_item = document.getElementById(element.id);

	var movie_index = -1;
	for (let index = 0; index < item_num_list.length; index++) {
		if(item_num_list[index] == element.id) {
			movie_index = index;
		}

	}

	if (movie_index != -1){
		liked_movies.splice(movie_index, 1);
		item_num_list.splice(movie_index, 1);
	}

	movie_item.remove();
 }

function submit() {
	fetch('/recommender_system', {method: 'POST', credentials: "include", body: JSON.stringify(liked_movies), cache: "no-cache", headers: new Headers({
      "content-type": "application/json"})})
      .then(function (response) {
          return response.json();
      }).then(function (text) {
          
      	  var movie_rec = text.movies;
          var movie_link = text.links;

          var ul = document.getElementById("recommended-list");
          ul.innerHTML = "";

          for (let index = 0; index < movie_rec.length; index++) {
          		
	  			var li = document.createElement("li");
	  			var a = document.createElement("a");

	  			title = movie_rec[index]

	  			max_length = 45

				if (title.length >= max_length) {
					title = title.slice(0,max_length-10) + "..." + title.slice(title.length - 6 ,title.length)
				}		

	  			a.innerHTML = title;

	  			a.setAttribute('href', movie_link[index]);
	  			a.setAttribute("target", "_blank");
	  			a.setAttribute('rel', "noopener noreferrer");
	  			a.style.color = "#0000CD";

	  			li.appendChild(a);
	  			ul.appendChild(li);
          }


      });
}
