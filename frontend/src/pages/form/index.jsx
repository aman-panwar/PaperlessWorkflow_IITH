import Header from '../../components/Header';
import { Box, Button, TextField, useTheme} from '@mui/material';
import { tokens } from '../../theme';
import { Formik } from 'formik';
import * as yup from "yup";
import useMediaQuery from '@mui/material/useMediaQuery';
import { useContext, useState } from 'react';
import { UserContext, FormSelectContext } from '../../App';
import { Navigate } from 'react-router-dom';
import MenuItem from '@mui/material/MenuItem';
import Modal from './Modal';

import Date from './fields/Date';
import File from './fields/File';
import Check  from './fields/Check';
import Dropdown from './fields/Dropdown';
import Text from './fields/Text';

const initialValues = {
    firstName: "",
    lastName: "",
    email: "",
    date: "",
};

// const emailRegExp = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
const formSchema = yup.object().shape({
    firstName: yup.string().required("required"),
    lastName: yup.string().required("required"),
    email: yup
            .string()
            // .matches(emailRegExp, "invalid email")
            .email("invalid email")
            .required("required"),
    date: yup.string().required()
});

const Form = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    const isNonMobile = useMediaQuery("(min-width:600px)");
    const { user } = useContext(UserContext);
    const { openFormModal, setOpenFormModal, formType, setFormType } = useContext(FormSelectContext);

    const handleFormSubmit = (values) => {
        console.log("Submitted Form!")
        console.log(values)
    }


    return (
        <>
        {!user ? <Navigate to='/login'/> : <></>}
        { openFormModal ? 
        <Modal open={openFormModal} onClose={()=>setOpenFormModal(false)}/>
        : formType ?
        <Box m="20px">
            {/* <Box display="flex" justifyContent="space-between" alignItems="center"> */}
            <Header title="FORM" subtitle="Enter the details and submit the form."/>
            <br></br>
            <Formik
                onSubmit={handleFormSubmit}
                initialValues={initialValues}
                validationSchema={formSchema}
            >
                {({ values, errors, touched, handleBlur, handleChange, handleSubmit }) => (
                    <form onSubmit={handleSubmit}>
                        <Box 
                            display="grid" 
                            gap="30px" 
                            gridTemplateColumns="repeat(4, minmax(0, 1fr))"
                            sx = {{
                                "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
                            }}
                        >
                            <Text label="First Name"/>
                            <Text label="Last Name"/>
                            <Text label="Email"/>
                            <Date/>
                            <Check />
                            <File/>
                            <Dropdown />
                        </Box>
                        <Box display="flex" justifyContent="end" mt="20px">
                            <Button type="submit" color="secondary" variant="contained" onClick={()=>setFormType(null)}>
                                Submit Form
                            </Button>
                        </Box>
                    </form>
                )}
            </Formik>
        </Box> 
        :
        <Navigate to='/'/>
        }
        </>
    );
    
}

export default Form;