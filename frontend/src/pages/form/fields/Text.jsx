import { TextField, FormControl } from '@mui/material';
import { useState } from 'react';
const Text = ({label}) => {

    const [value, setValue] = useState("");
    return(
        <FormControl sx={{gridColumn: "span 4"}}>
        <TextField
            fullWidth
            required
            variant="filled"
            type="text"
            label={label}
            autoComplete='off'
            // onBlur={handleBlur}
            onChange={(e) => setValue(e.target.value)}
            value={value}
            name={label}
            // error={!!touched.firstName && !!errors.firstName}
            // helperText={touched.firstName && errors.firstName}
            
        />
        </FormControl>
    );
}

export default Text;