import { useState } from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const Dropdown = ( { label, options }) => {

    const [value, setValue] = useState(null);

    const handleDropdownChange = (event) => {
        setValue(event.target.value.toString());
    }

    const renderMenuItems = () => {
        const items = []
        for(let i = 0; i < options.length; i++)
            items.push(<MenuItem value={options[i]}>{options[i]}</MenuItem>)
        return items;
    }

    return(
        <FormControl sx={{gridColumn: "span 2"}}>
            <InputLabel id="demo-multiple-name-label" color='secondary'>{label}</InputLabel>
            <Select
                // labelId="demo-simple-select-label"
                // id="demo-simple-select"
                value={value}
                label={label}
                onChange={handleDropdownChange}
                color='secondary'
            >
                {renderMenuItems()}
            </Select>
        </FormControl>
    );
}

export default Dropdown;