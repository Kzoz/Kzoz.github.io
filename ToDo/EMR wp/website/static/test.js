const searchInputSidenav = document.getElementById('search-input-sidenav');
const sidenavOptions = document.querySelectorAll('#sidenavigator li .sidenav-link');

searchInputSidenav.addEventListener('input', () => {
  const filter = searchInputSidenav.value.toLowerCase();
  showSidenavOptions();
  const valueExist = !!filter.length;

  if (valueExist) {
    sidenavOptions.forEach((el) => {
      const elText = el.textContent.trim().toLowerCase();
      const isIncluded = elText.includes(filter);
      if (!isIncluded) {
        el.style.display = 'none';
      }
    });
  }
});

const showSidenavOptions = () => {
  sidenavOptions.forEach((el) => {
    el.style.display = 'flex';
  });
};

  /* When the user clicks on the button, 
  toggle between hiding and showing the dropdown content */
  function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
        }
    }
    }
}

function deleteHistory(historyId){
  fetch('delete-history',{
    method: 'POST',
    body:JSON.stringify({historyId: historyId})
  }).then((_res) =>{
    window.location.href = '/details'+String(historyId)
  })
}