


function setTimerUi(seconds)
{
  if(seconds <= 0 ){
        document.getElementById('p').innerHTML= " Your Booking is expired Please re choose your seats "
        clearInterval(onGoing);
     }
else if( seconds >= 1 ){
    var second  = parseInt(seconds % 60)
    var minutes = parseInt(seconds / 60)
    document.getElementById('p').innerHTML=  `Your Booking Will Expire  In ${minutes}  : ${second}` 
    }
    
}



let countDown = () =>{

    var shit = parseInt( localStorage.getItem('timer'))
    // calling the method to check validitiy
    
    setTimerUi(shit)
        shit -= 1
        shit.toString()
        localStorage.setItem('timer',shit)
    
        
        
      
    }

    var onGoing =  setInterval(countDown,1200)  
   


let start = ()=>{
 let timer = 60
 localStorage.setItem( 'timer',timer)
 onGoing = setInterval(countDown,1200)  

}




