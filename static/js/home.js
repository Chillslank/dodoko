const arr = document.querySelectorAll('.home-list-group-item')
for (let i = 0; i < 5; i++) {
  arr[i].style.animationDelay = `${i * 0.2}s`    
  arr[i + 5].style.animationDelay = `${i * 0.2}s`    
  
}