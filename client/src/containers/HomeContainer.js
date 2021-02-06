import React from 'react';
import './HomeContainer.css'
import StockTable from './StockTableContainer'

function HomeContainer () {
    return (
        <div className = 'home-container'>
            <div className = 'navigation-bar'>
               <div className = 'title'>
                   Rookie Investor
               </div>
               <div className = 'menu-bar'>
                   Menu Bar
               </div>
            </div> 
            <div className = 'stock-table'>
                <StockTable />
            </div> 
            <div className = 'footer'>
                footer
            </div> 
        </div>
    )
}

export default HomeContainer