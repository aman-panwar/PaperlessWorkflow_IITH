import Header from '../../components/Header';
import { Box } from '@mui/material';

const FAQ = () => {
    return (
        <Box m="20px">
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header
                    title="FAQ"
                    subtitle="Here are some Frequently Asked Questions"
                />
            </Box>
        </Box>
    );
    
}

export default FAQ;