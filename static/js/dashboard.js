document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const companyListDiv = document.getElementById('companyList');
    const filterForm = document.getElementById('filterForm');

    const fetchCompanies = async () => {
        const response = await fetch('/api/companies');
        return await response.json();
    };

    const renderCompanies = (companies) => {
        companyListDiv.innerHTML = '';
        companies.forEach(company => {
            const companyCard = document.createElement('div');
            companyCard.classList.add('company-card');
            companyCard.innerHTML = `
                <div class="company-info">
                    <img src="${company.imgSrc}" alt="${company.name}">
                    <div>
                        <h2>${company.name}</h2>
                        <p class="company-details">${company.details}</p>
                        <button class="view-button" data-name="${company.name}">View</button>
                    </div>
                </div>
            `;
            companyListDiv.appendChild(companyCard);
        });

        document.querySelectorAll('.view-button').forEach(button => {
            button.addEventListener('click', (event) => {
                const companyName = event.target.dataset.name;
                viewCompanyDetails(companyName);
            });
        });
    };

    const filterCompanies = (companies, filters) => {
        return companies.filter(company => {
            return (!filters.price || company.price <= filters.price) &&
                (!filters.location || company.location.toLowerCase().includes(filters.location.toLowerCase())) &&
                (!filters.experience || company.experience >= filters.experience);
        });
    };

    const searchCompanies = (companies, query) => {
        return companies.filter(company => {
            return company.name.toLowerCase().includes(query.toLowerCase());
        });
    };

    const viewCompanyDetails = async (companyName) => {
        const companies = await fetchCompanies();
        const company = companies.find(c => c.name === companyName);
        if (company) {
            alert(`
                Name: ${company.name}
                Details: ${company.details}
                Location: ${company.location}
                Experience: ${company.experience}
                Price: ${company.price}
            `);
        }
    };

    searchButton.addEventListener('click', async () => {
        const query = searchInput.value.trim();
        const companies = await fetchCompanies();
        const filteredCompanies = searchCompanies(companies, query);
        renderCompanies(filteredCompanies);
    });

    filterForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const filters = {
            price: filterForm.price.value.trim() ? parseFloat(filterForm.price.value.trim()) : null,
            location: filterForm.location.value.trim(),
            experience: filterForm.experience.value.trim() ? parseInt(filterForm.experience.value.trim()) : null,
        };
        const companies = await fetchCompanies();
        const filteredCompanies = filterCompanies(companies, filters);
        renderCompanies(filteredCompanies);
    });

    // Initial render
    fetchCompanies().then(renderCompanies);
});
