import { Input, InputAdornment, IconButton } from '@mui/material';
import AttachmentIcon from '@mui/icons-material/Attachment';


const File = ({label}) => {
    return(
        <>
        <Input
            type="file"
            name="file"
            color='secondary'
            placeholder=""
            inputProps={{ multiple: true, title: "Upload a file" }}
            endAdornment={
                <InputAdornment position="end" >
                    {label}
                  <IconButton disableFocusRipple disableRipple style={{cursor: 'auto'}}>
                    <AttachmentIcon/>
                  </IconButton>
                </InputAdornment>
            }
            sx={{
                gridColumn: "span 2",
                padding: "10px",
                borderRadius: "5px",
            }}  
        />
        </>
    );
}

export default File;