import Header from '../../components/Header';
import { Box } from '@mui/material';

const Admin = () => {
    return (
        <Box m="20px">
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header
                    title="Admin"
                    subtitle="This is the Admin Panel"
                />
            </Box>
        </Box>
    );
    
}

export default Admin;