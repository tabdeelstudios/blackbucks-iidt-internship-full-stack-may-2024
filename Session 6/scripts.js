var taskList = document.getElementById("taskList");

const handleSubmit = (e) => {
  // don't perform any default tasks
  e.preventDefault();
  // detect the input field
  var taskInput = document.getElementById("task");
  // read the value entered by the user
  var userInput = taskInput.value;

  var newItem = document.createElement("li");
  newItem.innerHTML = "<p>" + userInput + "</p>";
  newItem.classList = ["listItem"];
  taskList.appendChild(newItem);

  taskInput.value = "";
};

const handleChangeBG = (e) => {
  e.target.style.backgroundColor = "pink";
};
