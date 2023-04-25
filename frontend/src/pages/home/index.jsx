import Header from '../../components/Header';
import { Box } from '@mui/material';

const Home = () => {
    return (
        <Box m="20px">
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header
                    title="HOME"
                    subtitle="Welcome to your homescreen"
                />
            </Box>
        </Box>
    );
    
}

export default Home;