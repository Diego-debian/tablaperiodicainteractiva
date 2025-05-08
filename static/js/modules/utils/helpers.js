/**
 * Módulo de funciones auxiliares generales
 */
const Helpers = {
    /**
     * Crea un elemento HTML con atributos
     * @param {string} tag - Etiqueta del elemento
     * @param {Object} attributes - Atributos a aplicar
     * @param {string|HTMLElement} content - Contenido del elemento
     * @returns {HTMLElement} Elemento creado
     */
    createElement: function(tag, attributes = {}, content = '') {
        const element = document.createElement(tag);
        
        // Aplicar atributos
        for (const [key, value] of Object.entries(attributes)) {
            element.setAttribute(key, value);
        }
        
        // Añadir contenido
        if (typeof content === 'string') {
            element.textContent = content;
        } else if (content instanceof HTMLElement) {
            element.appendChild(content);
        }
        
        return element;
    },
    
    /**
     * Formatea un número con separadores de miles
     * @param {number} number - Número a formatear
     * @returns {string} Número formateado
     */
    formatNumber: function(number) {
        return new Intl.NumberFormat().format(number);
    }
};

export default Helpers;