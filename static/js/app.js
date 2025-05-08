import Header from './modules/components/header.js';
import Footer from './modules/components/footer.js';
import Search from './modules/components/search.js';
import Legend from './modules/components/legend.js';
import PeriodicTable from './modules/components/periodic-table.js';
import DetailView from './modules/components/detail-view.js';

document.addEventListener('DOMContentLoaded', function() {
    console.log('Iniciando aplicación...');
    
    // Inicialización de componentes
    Header.init();
    Footer.init();
    
    // Determinar qué página estamos mostrando
    const periodicTable = document.querySelector('.periodic-table');
    const elementDetail = document.querySelector('.element-detail');
    
    if (periodicTable) {
        // Estamos en la página principal
        console.log('Inicializando tabla periódica');
        Search.init();
        Legend.init();
        PeriodicTable.init();
    }
    
    if (elementDetail) {
        // Estamos en la página de detalle
        console.log('Inicializando vista de detalle');
        DetailView.init();
    }
    
    // Actualizar el año en el footer automáticamente
    const currentYearSpan = document.getElementById('currentYear');
    if (currentYearSpan) {
        const year = new Date().getFullYear();
        currentYearSpan.textContent = year;
    }
});
