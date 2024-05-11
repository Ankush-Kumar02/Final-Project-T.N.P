document.querySelector('.menu-bar').addEventListener('click',function(){
    document.querySelector('.menu-bar').style.display = 'none';
    document.querySelector('.menu-close').style.display = 'block';
    document.querySelector('nav ul').style.display = 'block';
  });
  document.querySelector('.menu-close').addEventListener('click',function(){
    document.querySelector('.menu-close').style.display = 'none';
    document.querySelector('.menu-bar').style.display = 'block';
    document.querySelector('nav ul').style.display = 'none';
  });
  