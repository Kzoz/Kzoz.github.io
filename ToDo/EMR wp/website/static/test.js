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