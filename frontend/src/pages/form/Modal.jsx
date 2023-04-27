import { mockFormData } from "../../data/mockData";
import { Box, Typography, useTheme } from "@mui/material";
import { tokens } from '../../theme';
import { Link } from 'react-router-dom';
import { useContext, useState } from "react";
import { FormSelectContext } from "../../App";


const ListItem = ({displayName, uniqueName, link}) => {
    const theme = useTheme()
    const colors = tokens(theme.palette.mode);
    const { setFormType, setOpenFormModal } = useContext(FormSelectContext);

    const clickHandler = () => {
        setFormType(uniqueName); 
        setOpenFormModal(false);
    }

    
    return(
        <>
        <Link 
            to='/form'
            onClick={clickHandler}
            underline={false}
        >
            <Box
                display="flex" 
                justifyContent="center"
                alignItems="center"
                sx = {{
                    'border': '1px solid black',
                }}
            > 
                <Typography
                    variant="h4"
                    color={colors.grey[100]}
                    sx={{ m: "10px 10px 10px 10px",
                     }}
                    
                >{displayName}</Typography>
            </Box>
        </Link>
        </>
    );
}
const Modal = ({ open, onClose }) => {

    const theme = useTheme()
    const colors = tokens(theme.palette.mode);
    const formtypes = Object.keys(mockFormData); // ['formA', 'formB', 'formC']
    const [dataSource, setDataSource] = useState(formtypes.slice(0, 6))
    const fetchMoreData=() => {
        // Get the current length of the dataSource array
        const currentLength = dataSource.length;

        // Get the next 6 elements from the formtypes array
        const nextElements = formtypes.slice(currentLength, currentLength + 6);

        // Update the dataSource state to include the next 6 elements
        setDataSource([...dataSource, ...nextElements]);
    }
    if (!open) return null;
    return(
        <>
        <Box
            display = "flex"
            flexDirection="column"
            border="2px solid black"
            borderRadius="10px"
            width="30%"
            marginLeft="35%"
            marginRight="35%"
            height="50%"
            marginTop="10%"
            backgroundColor={colors.primary[400]}
        >
            <Box 
                display='flex' 
                justifyContent="space-between" 
                alignItems="center"
                sx = {{ m: "10px 10px 10px 10px"}}
            >
            <Typography variant="h3" color={colors.grey[100]} sx = {{m: "0px 10px 0px 10px"}}>
                Select a form type
            </Typography>
            <Typography variant="h3" color={colors.grey[100]} sx = {{m: "0px 10px 0px 10px"}}
                onClick={onClose}
            >
                x
            </Typography>
            
            </Box>
            <Box 
                display="flex" 
                flexDirection="column" 
                alignItems="center"
                sx = {{
                    m : "10px 0px 10px 0px", 
                    overflowY:"scroll", 
                    p:"0px 0px 0px 0px",
                    '&::-webkit-scrollbar-track': {
                        backgroundColor: colors.primary[400],
                    },
                    '&::-webkit-scrollbar-thumb': {
                        backgroundColor: colors.primary[300],
                    }
                }}
                height="100%"
                // border="2px solid black"
                
                
            >
            { formtypes.map((form, i) => (
                <ListItem displayName={mockFormData[formtypes[i]]['name']} uniqueName={formtypes[i]}/>
            ))}
            </Box>
        </Box>
        </>
        
    );
}

export default Modal;