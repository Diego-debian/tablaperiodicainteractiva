/**
 * Módulo para gestionar la funcionalidad de la leyenda
 */
const Legend = {
    init: function() {
        console.log('Inicializando módulo de leyenda');
        this.bindEvents();
    },
    
    bindEvents: function() {
        const legendBtn = document.getElementById('legendBtn');
        const legendContainer = document.getElementById('legendContainer');
        
        if (legendBtn && legendContainer) {
            legendBtn.addEventListener('click', () => {
                this.toggleLegend(legendContainer);
            });
            
            // Cerrar leyenda con ESC
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape' && legendContainer.style.display === 'block') {
                    legendContainer.style.display = 'none';
                }
            });
        }
    },
    
    toggleLegend: function(legendContainer) {
        legendContainer.style.display = legendContainer.style.display === 'block' ? 'none' : 'block';
    }
};
document.getElementById('legendContainer').style.display = 'block';
export default Legend;