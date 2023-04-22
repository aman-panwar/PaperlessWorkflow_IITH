import Header from '../../components/Header';
import { Box } from '@mui/material';

const Form = () => {
    return (
        <Box m="20px">
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header
                    title="Form"
                    subtitle="Enter the details and submit the form."
                />
            </Box>
        </Box>
    );
    
}

export default Form;