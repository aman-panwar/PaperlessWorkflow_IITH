import { useState } from 'react';
import { FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const Dropdown = () => {

    const [dropdown, setDropdown] = useState(null);

    const handleDropdownChange = (event) => {
        setDropdown(event.target.value.toString());
    }

    return(
        <FormControl>
            <InputLabel id="demo-multiple-name-label" color='secondary'>Age</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={dropdown}
                label="Age"
                onChange={handleDropdownChange}
                color='secondary'
            >
                <MenuItem value={10}>Ten</MenuItem>
                <MenuItem value={20}>Twenty</MenuItem>
                <MenuItem value={30}>Thirty</MenuItem>
            </Select>
        </FormControl>
    );
}

export default Dropdown;