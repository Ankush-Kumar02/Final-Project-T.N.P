window.onload = function() {
    // Code to be executed when the page is loaded
    // You can access and manipulate DOM elements here
    // Example:
    hide_all_syllabus();
    document.getElementById('section-1').style.display = "block";
    const adca = document.querySelector('#section-1')
    adca.style.marginLeft = "120px";

  };
  
    

//I have determined the constant of some calss function
var li_item = document.querySelectorAll(".sidebar ul li");
// var hamburger = document.querySelector(".hamburger");
var wrapper = document.querySelector(".wrapper");

//what will chage if you move the mouse over the sidebar 
li_item.forEach((li_item)=>{
    li_item.addEventListener("mouseenter", ()=>{
        //I have already add style informatio about hover_collapse
        li_item.closest(".wrapper").classList.remove("hover_collapse");
        //in general, hover_collapse will be applied on the sidebar
        const java = document.querySelector('#section-9')
        const adca = document.querySelector('#section-1')
        const dca = document.querySelector('#section-2')
        const dtp = document.querySelector('#section-3')
        const tally = document.querySelector('#section-4')
        const dctt = document.querySelector('#section-5')
        const web = document.querySelector('#section-6')
        const pgdca = document.querySelector('#section-7')
        const cc = document.querySelector('#section-8')

        java.style.marginLeft = "240px";
        adca.style.marginLeft = "240px";
        dca.style.marginLeft = "240px";
        dtp.style.marginLeft = "240px";
        tally.style.marginLeft = "240px";
        dctt.style.marginLeft = "240px";
        web.style.marginLeft = "240px";
        pgdca.style.marginLeft = "240px";
        cc.style.marginLeft = "240px";

        
        //hover_collapse will be remover from the sidebar when the mouse is moved
    })
});
li_item.forEach((li_item)=>{
    li_item.addEventListener("mouseleave", ()=>{
        //hover_collapse will be applied again when the mouse is removed
        li_item.closest(".wrapper").classList.add("hover_collapse");
        const java = document.querySelector('#section-9')
        const adca = document.querySelector('#section-1')
        const dca = document.querySelector('#section-2')
        const dtp = document.querySelector('#section-3')
        const tally = document.querySelector('#section-4')
        const dctt = document.querySelector('#section-5')
        const web = document.querySelector('#section-6')
        const pgdca = document.querySelector('#section-7')
        const cc = document.querySelector('#section-8')

        java.style.marginLeft = "120px";
        adca.style.marginLeft = "120px";
        dca.style.marginLeft = "120px";
        dtp.style.marginLeft = "120px";
        tally.style.marginLeft = "120px";
        dctt.style.marginLeft = "120px";
        web.style.marginLeft = "120px";
        pgdca.style.marginLeft = "120px";
        cc.style.marginLeft = "120px";
        //in general, hover_collapse will be applied on the sidebar

        //hover_collapse will be remover from the sidebar when the mouse is moved
    })
});

// now i will execute menu bars buttons
// hamburger.addEventListener("click",()=>{
//     hamburger.closest(".wrapper").classList.toggle("hover_collapse");
// });



function hide_all_syllabus()
{
    const sec = document.querySelectorAll('section');
    sec.forEach((section)=>{
        section.style.display = "none";
            
    })
}

function show_syllabus1() {
    hide_all_syllabus();
    document.getElementById("section-1").style.display= "block";    
}
function show_syllabus2() { 
    hide_all_syllabus();
    document.getElementById("section-2").style.display = "block";  
}

function show_syllabus3() { 
    hide_all_syllabus();
    document.getElementById("section-3").style.display = "block";  
}
function show_syllabus4() { 
    hide_all_syllabus();
    document.getElementById("section-4").style.display = "block";  
}
function show_syllabus5() { 
    hide_all_syllabus();
    document.getElementById("section-5").style.display = "block";  
}
function show_syllabus6() { 
    hide_all_syllabus();
    document.getElementById("section-6").style.display = "block";  
}
function show_syllabus7() { 
    hide_all_syllabus();
    document.getElementById("section-7").style.display = "block";  
}
function show_syllabus8() { 
    hide_all_syllabus();
    document.getElementById("section-8").style.display = "block";  
}
function show_syllabus9() { 
    hide_all_syllabus();
    document.getElementById("section-9").style.display = "block";  
}