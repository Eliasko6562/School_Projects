const continent = document.getElementById('continent');
const modal = new bootstrap.Modal(document.getElementById('windowCountry'));
const modalHeader = document.getElementById("modal-header-content");
const modalBody = document.getElementById("modal-body-content");
const modalFooter = document.getElementById("modal-footer-content");

function formatNum(num) {
  return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, "&nbsp;");
}

function displayValue(value, formatter = v => v) {
  if (!value) return '--';
  if (Array.isArray(value)) return value.length ? value.map(formatter).join(', ') : '--';
  if (typeof value === 'object') return Object.values(value).length ? Object.values(value).map(formatter).join(', ') : '--';
  return formatter(value);
}

function hasMore(value) {
  return Object.values(value).length > 1 ? 's' : '';
}

document.addEventListener('DOMContentLoaded', function () {
  const btn = document.getElementById('mapsRedirectBtn');
  btn.addEventListener('click', function () {
    // Assumes you set country name in modal-header-content
    const country = document.getElementById('modal-header-content').textContent.trim();
    if (country) {
      window.open(`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(country)}`, '_blank');
    }
  });
});

async function getData(region) {
  const url = `https://restcountries.com/v3.1/region/${region}`;
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);
    let blocks = '';
    json.forEach((country) => {
      blocks += `
        <div class="col-xl-2 col-lg-3 col-md-4 col-sm-6">                
          <div class="card bg-dark text-white mb-3 border-0">
            <img class="card-img-top" src="${country.flags.png}" alt="Vlajka" style="height: 160px;">
            <div class="card-body">
              <h4 class="card-title"><strong>${country.name.common} (${country.cca3})</strong></h4>
              <p class="card-text"><strong>Population:</strong> ${formatNum(country.population)}</p>
              <a href="#" class="btn btn-secondary card-link border-0 text-black" 
                 data-name="${country.name.common}">Information</a>
            </div>
          </div>
        </div>            
      `;
    });
    listCountries.innerHTML = blocks;

    document.querySelectorAll('[data-name]').forEach(button => {
      button.addEventListener('click', () => {
        const countryName = button.getAttribute('data-name');
        modal.show();
        fetch(`https://restcountries.com/v3.1/name/${countryName}`)
          .then((res) => res.json())
          .then((data) => {
            const country = data[0];

            if (country.borders === undefined) {
              country.borders = [];
            }

            modalHeader.innerHTML = `<h2><strong>${country.name.common}</strong></h2>`;
            modalBody.innerHTML = `
              <ul>
                <li> <strong>Capital:</strong> ${displayValue(country.capital)}
                <li> <strong>Population:</strong> ${formatNum(country.population)}
                <li> <strong>Area:</strong> ${formatNum(country.area)} km<sup>2</sup>
                <li> <strong>Subregion:</strong> ${displayValue(country.subregion)}
                <li> <strong>Currency:</strong> ${displayValue(country.currencies, c => c.name)} (${displayValue(country.currencies, c => c.symbol)})
                <li> <strong>Language${hasMore(country.languages)}:</strong> ${displayValue(country.languages)}
                <li> <strong>Neighbor${hasMore(country.borders)}:</strong> ${displayValue(country.borders)}
                <li> <strong>Timezone${hasMore(country.timezones)}:</strong> ${displayValue(country.timezones)}
              </ul>
            `;
            modalFooter.innerHTML = `
              <div class="d-flex align-items-center w-100">
                <img src="${country.flags.png}" alt="Vlajka" class="me-3" style="height: 60px;">
                <div class="flex-grow-1"></div>
                <button type="button" class="btn btn-danger ms-auto" data-bs-dismiss="modal">Close</button>
              </div>
            `;
          })
          .catch(error => {
            console.log(`Nastala chyba: ${error}`);
          });
      });
    });
  } catch (error) {
    console.error(error.message);
  }
}

continent.addEventListener('change', () => {
  getData(continent.value);
});

getData('europe');
