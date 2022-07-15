document.body.style.backgroundColor = 'green';

// display toggle for admin menu
document.getElementById("admin-btn").addEventListener('click', ()=>{
  let adminMenu = document.getElementById("admin-menu")
  adminMenu.style.display === "none"? adminMenu.style.display = "block" : adminMenu.style.display = "none";
})

