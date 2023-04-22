import Header from '../../components/Header';
import { Box } from '@mui/material';

const Table = () => {
    return (
        <Box m="20px">
            <Box display="flex" justifyContent="space-between" alignItems="center">
                <Header
                    title="TABLE"
                    subtitle="List of active forms"
                />
            </Box>
        </Box>
    );
    
}

export default Table;