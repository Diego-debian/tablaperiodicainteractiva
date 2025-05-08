/**
 * Módulo para gestionar la tabla periódica
 */
const PeriodicTable = {
    init: function() {
        console.log('Inicializando tabla periódica');
        this.addHoverEffects();
    },
    
    addHoverEffects: function() {
        const elements = document.querySelectorAll('.element');
        let hoverTimer;
        
        elements.forEach(element => {
            element.addEventListener('mouseenter', function() {
                hoverTimer = setTimeout(() => {
                    this.style.transform = 'scale(1.1)';
                    this.style.zIndex = '100';
                    this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.2)';
                }, 100);
            });
            
            element.addEventListener('mouseleave', function() {
                clearTimeout(hoverTimer);
                this.style.transform = '';
                this.style.zIndex = '';
                this.style.boxShadow = '';
            });
        });
    }
};

export default PeriodicTable;