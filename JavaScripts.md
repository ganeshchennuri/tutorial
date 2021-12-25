# JavaScript
- A weakly typed, interpreted language
- Built into browsers, runs on Javascript Engines (Chrome V8, Firefox SpiderMonkey)
- Js Engine Parses Code, Compiles to machine code & Executes it (single Thread).
- V8 Engine extracted to run js anywhere (NodeJs), can access file system & used tp build backends
- ECMA(Europian Computers Manufacture Association) creates a standards in form of ECMAScript and are implemented in JS engines like V8.

## Variables & Constants
- variables declared using let keyword and values can be changed
    ```js
    let firstName = 'Arya'
    firstName = 'Sansa'
    ```
- variable declared with const keyword has constant value and cannot be changed
    ```js
    const totalUsers = 15 
    //Cannot be reassigned using varible name  totalUsers = 10 
    ```

### Variable naming conventions
- camel case -> userName
- only letters and digits -> ageGroup2
- starting with dollar and underscore is allowed -> $name, _isExact
- snake case is not recommended & variables must not start with numbers & shouldn't have special characters in between (eg. user-name)
- keywords are not allowed for variable names


## DataTypes
- integer, float, Strings, boolean, undefined, null

## Other func
- alert("hello world")
- prompt("Enter Anyting")
- clear()
- .length()

---
## Variables
- var x = 5;
- var x = 'yes';
- var x = true;

var y; -> undefined(variable created but never defined)
var y = null; -> variable value set to nothing
let x = 5 similar to var (replacement of var)

const x = 10; => Once defined cannot be changed

---
## comparison
```
2 == "2" -> true (due to inbuilt type conversion)
2 === "2" -> false (comparison with data type)
2 != "2" -> false
2 !== "2" -> true
```
- Logical Operators (&&, ||, !(), )
---
## For loops
- for -> normal loopong
- for in -> looping js objects
	```
	objects = {
		"lang": "Python",
		"version":3.8,
		"framework":"django"
		};
	for(obj in objects){
		console.log(obj);
		console.log(objects[obj]);
	}
	```
- for of -> for arrays
	```
	numbers = [1,2,3,4]
	for(num of numbers){
		console.log(num)
	}
	```
- forEach
	```
	names = ["sai", "Arbaaz","NoOne]
	names.forEach(alert)
	```
---
## Function
name = 'Ajay'
function greet(name="Nobody"){
  console.log("Hello "+ name)
}

function code is returned if only name is specified (without parenthesis)

x = (name) => {
return "Hello"+name
}

y = () => 2+3

z = (a,b) => a+b

---

## Object

Dictionary in python is an object in JS
conat person = {
	name : "James",
	Age : 23,
	greet(){ 
		console.log("Hello " + this.name);
	}
}

---

## Array

const arr = [1, 'a', "Hell"]
const hobbies = ['Sports', 'Cooking']

hobbies.append('Gaming')

- arrays can be modiefied even after defining as constant since memory location is at same place

### Nested Array
- const copiedarray = [hobbies] 

---

## Spread operator(unpacking)
- const copiedarray = [...hobbies] 

- for objects also the same unpacking occurs
console.log(...person)	-> displays only values

> const toArray = (arg1, arg2) => {
return [arg1, arg2]
}

## Rest operator same but in arow function
- No given number of params
```js
const toArray = (...args) => {
return args
}

const Data = (person) => {
console.log(person.name)
}

cpnst Data = ({ name }) => {
console.log(name);
}

const { name, age } = person;
console.log(name,age)
```

# DOM (Document Object Model)
- dir(document) -> represents html page as javascript objects
- document.URL, document.body, document.head, document.links
- document.querySelector() -> returns first matching css style (#for id, . for class)
- document.querySelectorAll() -> returns all matches
- HTMLElement.textContent(), element.inerHTML(), .getAttribute(), .setAttribute()
- element.addEventListeners("click",functtion(){
	element.style.color = "Red";
})
- other listeners, mouseover,mouseout,dbclick,etc

# JQuery
- JS library, single.js file that has many pre-built methods and objects, specific fo interacting DOM Objects
	```
	Examples
	var divs = $('div') //JQuery
	var divs =  document.querySelectorAll("div) //Vanilla JS

	$(el).css("border-width","20px");
	el.style.borderWidth = "20px";

	$(document).ready(function(){//Code})
	function ready(fn){
	if (document.readyState != 'loading'){
		fn();
	}else{
		document.addEventListener('DOMContentloaded',fn)
	}}
	```
- Some of the examples in dev tools
	```
	$
	=> ƒ (a,b){return new r.fn.init(a,b)}

	var x = $('h1');
	x.css('color','blue')
	```
	- we can pass js objects as css parameters for changing multiple properties
	```
	var prop = {
		'color': 'white',
		'background-color': 'green',
		'border': '5px solid red'
	}
	x.css(prop);
	```
- multiple items list for eg.
	```
	var li_items = $('li');
	li_items.css('color','blue');
	li_items.eq(0).css('color','orange');
	```
- Text and HTML items
	```
	$('h1').text()
	"Selecting with jQuery"

	$('h1').text('Hell Yeah');

	$('h1').html()
	"Hell Yeah"

	$('h1').html('<em>Boi</em>');
	```
- Changing Attributes
	```
	//Submit button to checkbox
	var inpu = $('input');
	inpu.eq(1).attr('type','checkbox');
- Ading and removing classes
	```
	$('h1').addClass('turnRed');
	$('h1').removeClass('turnRed');
	// if already present then remove add if not present already
	$('h1').toggleClass('turnRed');
	```
- Click events JQuery, key pressed
	```
	$('h1').click(function(){
		$(this).text('Heading 1 is clicked');
	})

	// pressing any key will toggle h3 background
	$('input').eq(0).keypress(function(){
	$('h3').toggleClass('turnBlue');
	})

	// Pressing Enter will toggle h3
	$('input').eq(0).keypress(function(event){
		if (event.which == 32){
			$('h3').toggleClass('turnBlue');
		}
	})
	```
- On function for dublelick
	```
	$('h1').on('dblclick',function(){
		$(this).toggleClass('turnRed');
	})

	//mouse over
	$('h1').on('mouseenter',function(){
		$(this).toggleClass('turnRed');
	})

	// Animations
	$('input').eq(1).on('click',function(){
		$('.container').fadeOut(3000)
	})

	$('input').eq(1).on('click',function(){
		$('.container').slideUp(3000)
	})
	```s