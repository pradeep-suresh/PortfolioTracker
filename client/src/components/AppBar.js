import React from 'react'
import MenuIcon from '@material-ui/icons/Menu';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import './AppBar.css'

export default function AppBar() {
    return(
        <div className='app-bar'>
            <div className='menu'>
                <MenuIcon style={{ color: 'gray'}} />
            </div>
            <div className='account-icons'>
                <AccountCircleIcon style={{ color: 'gray'}} />
            </div>
        </div>

    )
}

