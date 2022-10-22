let body = document.querySelector('body')
let displayBus = document.querySelector('.buses')
let busList = document.createElement('ul')
const lists = displayBus.appendChild(busList)
let searchInputField = document.getElementById('search-box')

// you only want to show the  bus suggestion when the user is searching

const gitHubUsers = async()=>{
  const url = `api/bus-brand/`
  // const url = 'https://api.github.com/users'
 
  const buses = await fetch(url).then((response)=>response.json())
  
  body.addEventListener('click',()=>{
    if(document.activeElement.id == searchInputField.id){ 
        displayBus.style.display = "block" }
   
   else{displayBus.style.display = "none"}});
   

   searchInputField.addEventListener('input',()=>{
    let searchedValue = searchInputField.value
   
    // JUST REPLACE YOUR JSON NAME HERE 
    
    const filteredUser = buses.filter((bus)=>{
   return bus.name.includes(searchedValue);
     });
   console.log(filteredUser);
   
   
     //removing the suggestion after the user changes the input
     const userItems = document.querySelectorAll('.suggestions')
   if(userItems){userItems.forEach((userItem)=>{ userItem.remove()});}
   
   
   
   // removing the not found warning , after the user changes the input
   const notFound = document.querySelector('.notFound')
     if(notFound){notFound.remove()}
    
   
   
   if(filteredUser.length){
   filteredUser.forEach((bus)=>{
   const li = document.createElement('li')
   console.log(bus.name)
   li.innerHTML = `${bus.name}` ;
   li.className = "suggestions";
   li.style.cursor = "pointer";
   // adding event listener
   li.addEventListener('click',()=>{
       searchInputField.value = li.innerHTML;
       document.searchForm.submit()
   });
   lists.appendChild(li)});}
   
   
   
   else{
      const warning = document.createElement('p')
       warning.innerHTML = " The Bus cannot be found !!"
       warning.className = "notFound";
       lists.appendChild(warning)}
   });
   

}

gitHubUsers();
