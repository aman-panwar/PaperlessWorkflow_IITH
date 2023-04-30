import { useState } from 'react';
import { Checkbox, FormControlLabel } from '@mui/material';

const Check = ({label}) => {

    const [checked, setChecked] = useState(false);

    const handleChange = (newValue) => {
        setChecked(newValue);
    }

    return(
        <FormControlLabel 
            control={<Checkbox defaultChecked={false} color='secondary'/>} 
            label={label}
            value={checked}
            onChange={handleChange} 
            sx ={{ gridColumn: "span 4" }}
        />
    );
}

export default Check;