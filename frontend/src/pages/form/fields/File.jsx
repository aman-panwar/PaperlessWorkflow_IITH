import { Input } from '@mui/material';

const File = () => {
    return(
        <Input
            type="file"
            name="file"
            color='secondary'
            inputProps={{ multiple: true }}
            sx={{
                gridColumn: "span 2",
                padding: "10px",
                borderRadius: "5px",
            }}  
        />
    );
}

export default File;