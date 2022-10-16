let displayer  = document.getElementById('countDownDiv');
let  setTimerUi = (seconds) =>
{
  if(seconds <= 0 ){
    displayer.innerHTML= " Your Booking is expired Please re choose your seats ";
        clearInterval(onGoing);
    }
else if( seconds >= 1 ){
    var second  = parseInt(seconds % 60)
    var minutes = parseInt(seconds / 60)
    displayer.innerHTML=  ` Your Booking Will Expire  In ${minutes}  : ${second} ` ;
    }
}



let countDown = () =>{

    let timeSince  = parseInt( localStorage.getItem('timer'))
    // calling the method to check validitiy
        timeSince -= 1
        timeSince.toString()
        localStorage.setItem('timer',timeSince) 
        setTimerUi(parseInt(timeSince)) 
        if(parseInt(timeSince)< 0){
          localStorage.removeItem('timer')  
        }    
 }
let onGoing =  setInterval(countDown,1200); 
   

if(document.getElementById('bookingForm')){
    document.getElementById('bookingForm').addEventListener('submit',()=>{
     let timer = 60
     localStorage.setItem( 'timer',timer)
     onGoing = setInterval(countDown,1200)  
    });}


if(document.getElementById('a')){
    document.getElementById('a').addEventListener('submit',()=>{
        displayer.innerHTML= "Payment Information sent! We will contact you soon ";
        localStorage.removeItem('timer');
        clearInterval(onGoing);
        console.log("working")
       
        
  
  });
}





