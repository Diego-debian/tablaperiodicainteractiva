/**
 * Módulo de utilidades para animaciones
 */
const Animations = {
    /**
     * Aplica una animación de entrada suave
     * @param {HTMLElement} element - Elemento al que aplicar la animación
     */
    fadeIn: function(element) {
        if (!element) return;
        element.style.opacity = '0';
        element.classList.add('fade-in');
        setTimeout(() => {
            element.style.opacity = '1';
        }, 50);
    },
    
    /**
     * Aplica una animación de salida suave
     * @param {HTMLElement} element - Elemento al que aplicar la animación
     * @param {Function} callback - Función a ejecutar al terminar la animación
     */
    fadeOut: function(element, callback) {
        if (!element) return;
        element.style.opacity = '1';
        element.style.transition = 'opacity 0.3s ease';
        element.style.opacity = '0';
        
        setTimeout(() => {
            if (typeof callback === 'function') {
                callback();
            }
        }, 300);
    }
};

export default Animations;
