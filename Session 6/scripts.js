// Example 1
// fetch("http://randomuser.me/api").then((response) =>
//   response.json().then((data) => {
//     var userImg = document.getElementById("userImage");
//     var userName = document.getElementById("userName");
//     var loading = document.getElementById("loading");

//     userImg.setAttribute("src", data.results[0].picture.thumbnail);
//     userName.innerHTML = data.results[0].name.first;
//     loading.style.display = "none";
//   })
// );

// Example 2
function fetchBooks() {
  var bookTitle = document.getElementById("bookTitle").value;

  // Add a dyanmic src attribute
  var books = document.getElementById("books");

  fetch("https://www.googleapis.com/books/v1/volumes?q=" + bookTitle).then(
    (response) =>
      response.json().then((data) => {
        data.items.map((book) => {
          var bookImage = document.createElement("img");
          bookImage.setAttribute("src", book.volumeInfo.imageLinks.thumbnail);
          books.appendChild(bookImage);
        });
      })
  );
}

// fetch("http://randomuser.me/api", {
//   headers: { API_KEY: "myKEY" },
// });
