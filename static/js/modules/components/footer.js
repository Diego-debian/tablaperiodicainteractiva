/**
 * Módulo para gestionar el comportamiento del pie de página
 */
const Footer = {
    init: function() {
        console.log('Inicializando componente Footer');
        this.updateYear();
    },
    
    updateYear: function() {
        const yearElement = document.getElementById('currentYear');
        if (yearElement) {
            yearElement.textContent = new Date().getFullYear();
        }
    }
};

export default Footer;