const inputBox = document.getElementById("input_box");
const listContainer = document.getElementById("list-container");

function addTask(){
    if(inputBox.value === ''){
        alert("You must write some task!!!");
    }
    else{
        let li = document.createElement("li"); //creating element with <li> tag and storing it in the const li variable
        li.innerHTML = inputBox.value; //text written it the input field will be stored in this variable
        listContainer.appendChild(li); //this li element will be displayed in the listContainer

        let span = document.createElement("span");
        span.innerHTML = '';
        li.appendChild(span);
    }
    inputBox.value = "";
    saveData();
}

listContainer.addEventListener("click", function (e){
    if(e.target.tagName === "LI"){
        e.target.classList.toggle("checked");
        saveData();
    }
    else if(e.target.tagName === "SPAN"){
        e.target.parentElement.remove();
        saveData();
    }
}, false);

function saveData(){
    localStorage.setItem("data", listContainer.innerHTML);
}

function showTask(){
    listContainer.innerHTML = localStorage.getItem("data");
}
showTask();
