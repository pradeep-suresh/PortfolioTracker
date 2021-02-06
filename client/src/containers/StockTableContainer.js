import React from 'react'
import './StockTableContainer.css'


function TableHeader() {
    let headers = ['Symbol', 'Price', 'Day Gain(%)', 'Day Gain($)', 'Volume']
    return (
        headers.map((value, index) => {
            return <th key={index}> {value} </th>
        })
    )
}

function StockTable() {
    return (
        <table className='container-table'>
            <thead>
                <tr>
                    <TableHeader />
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AAPL</td>
                    <td>136.6</td>
                    <td>-0.31</td>
                    <td>-0.425</td>
                    <td>72317009</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>136.6</td>
                    <td>-0.31</td>
                    <td>-0.425</td>
                    <td>72317009</td>
                </tr>
                <tr>
                    <td>AAPL</td>
                    <td>136.6</td>
                    <td>-0.31</td>
                    <td>-0.425</td>
                    <td>72317009</td>
                </tr>
            </tbody>
        </table>
    )
}

export default StockTable