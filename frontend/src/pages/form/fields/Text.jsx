import { TextField } from '@mui/material';
const Text = ({label}) => {
    return(
        <TextField
            fullWidth
            variant="filled"
            type="text"
            label={label}
            // onBlur={handleBlur}
            // onChange={handleChange}
            // value={values.firstName}
            name={label}
            // error={!!touched.firstName && !!errors.firstName}
            // helperText={touched.firstName && errors.firstName}
            sx ={{ gridColumn: "span 4" }}
        />
    );
}

export default Text;