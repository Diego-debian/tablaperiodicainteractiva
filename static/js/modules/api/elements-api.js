/**
 * Módulo para manejar las peticiones a la API de elementos
 */
const ElementsAPI = {
    /**
     * Obtiene todos los elementos
     * @returns {Promise} Promesa con los datos de los elementos
     */
    getAllElements: async function() {
        try {
            const response = await fetch('/api/elementos');
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error('Error al cargar elementos:', error);
            throw error;
        }
    },
    
    /**
     * Obtiene un elemento por su número atómico
     * @param {number} number - Número atómico del elemento
     * @returns {Promise} Promesa con los datos del elemento
     */
    getElementById: async function(number) {
        try {
            const response = await fetch(`/api/elementos/${number}`);
            if (!response.ok) {
                throw new Error(`Error: ${response.status}`);
            }
            return await response.json();
        } catch (error) {
            console.error(`Error al cargar elemento ${number}:`, error);
            throw error;
        }
    },
    
    /**
     * Busca elementos por término de búsqueda
     * @param {string} term - Término de búsqueda
     * @returns {Promise} Promesa con los elementos filtrados
     */
    searchElements: async function(term) {
        if (!term) return [];
        term = term.toLowerCase();
        
        try {
            // Obtenemos todos los elementos y filtramos en el cliente
            // Si hay muchos elementos, esto debería moverse al servidor
            const elementos = await this.getAllElements();
            
            return elementos.filter(elemento => 
                elemento.number.toString().includes(term) || 
                elemento.name.toLowerCase().includes(term) || 
                elemento.symbol.toLowerCase().includes(term)
            );
        } catch (error) {
            console.error(`Error al buscar elementos con el término: ${term}`, error);
            throw error;
        }
    }
};

export default ElementsAPI;