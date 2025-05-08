import ElementsAPI from '../api/elements-api.js';

/**
 * Módulo para gestionar la funcionalidad de búsqueda
 */
const Search = {
    init: function() {
        console.log('Inicializando módulo de búsqueda');
        this.bindEvents();
    },
    
    bindEvents: function() {
        const searchInput = document.getElementById('searchInput');
        const searchBtn = document.getElementById('searchBtn');
        
        if (searchInput && searchBtn) {
            // Eventos de búsqueda
            searchBtn.addEventListener('click', this.performSearch.bind(this));
            searchInput.addEventListener('keyup', (e) => {
                if (e.key === 'Enter') {
                    this.performSearch();
                }
            });
        }
    },
    
    performSearch: async function() {
        const searchInput = document.getElementById('searchInput');
        if (!searchInput) return;
        
        const searchTerm = searchInput.value.toLowerCase();
        if (!searchTerm) {
            // Si la búsqueda está vacía, mostrar todos los elementos
            document.querySelectorAll('.element').forEach(el => {
                el.style.display = 'flex';
            });
            return;
        }
        
        try {
            // En vez de usar la API directamente para la búsqueda,
            // hacemos la búsqueda local en los elementos ya renderizados
            // para evitar recargar la página
            const elements = document.querySelectorAll('.element');
            
            elements.forEach(element => {
                const number = element.getAttribute('data-number');
                const name = element.getAttribute('data-name').toLowerCase();
                const symbol = element.getAttribute('data-symbol').toLowerCase();
                
                if (number.includes(searchTerm) || name.includes(searchTerm) || symbol.includes(searchTerm)) {
                    element.style.display = 'flex';
                    element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                } else {
                    element.style.display = 'none';
                }
            });
        } catch (error) {
            console.error('Error en la búsqueda:', error);
            alert('Ocurrió un error al buscar elementos');
        }
    }
};

export default Search;
