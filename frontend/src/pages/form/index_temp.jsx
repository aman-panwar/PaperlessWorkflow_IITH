import Header from '../../components/Header';
import { Box, Button, TextField, Checkbox, FormControlLabel, Input, useTheme, FormControl, InputLabel} from '@mui/material';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import { DatePicker } from '@mui/x-date-pickers';
import { tokens } from '../../theme';
import { Formik } from 'formik';
import * as yup from "yup";
import useMediaQuery from '@mui/material/useMediaQuery';
import { useContext, useState } from 'react';
import { UserContext, FormSelectContext } from '../../App';
import { Navigate } from 'react-router-dom';
import MenuItem from '@mui/material/MenuItem';
import Modal from './Modal';

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

    const [date, setDate] = useState(null);
    const [checked, setChecked] =useState(false);
    const [dropdown, setDropdown] = useState(null);

    const changeDate = (newDate) => {
        setDate(newDate);
    }

    const handleDropdownChange = (event) => {
        setDropdown(event.target.value.toString());
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
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="First Name"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.firstName}
                                name="firstName"
                                error={!!touched.firstName && !!errors.firstName}
                                helperText={touched.firstName && errors.firstName}
                                sx ={{ gridColumn: "span 2" }}
                            />
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="Last Name"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.lastName}
                                name="lastName"
                                error={!!touched.lastName && !!errors.lastName}
                                helperText={touched.lastName && errors.lastName}
                                sx ={{ gridColumn: "span 2" }}
                            />
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="Email"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.email}
                                name="email"
                                error={!!touched.email && !!errors.email}
                                helperText={touched.email && errors.email}
                                sx ={{ gridColumn: "span 4" }}
                            />
                            <DatePicker
                                value ={date}
                                onChange={changeDate}
                                color='secondary'
                                sx ={{ gridColumn: "span 1" }} 
                            />
                            <FormControlLabel 
                                control={<Checkbox defaultChecked={false} color='secondary'/>} 
                                label="I agree to the terms and conditions."
                                value={checked}
                                onChange={()=>{setChecked(!checked); console.log(checked);}} 
                                sx ={{ gridColumn: "span 4" }}
                            />
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
                            <FormControl>
                            <InputLabel id="demo-multiple-name-label" color='secondary'>Age</InputLabel>
                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={dropdown}
                                label="Age"
                                onChange={handleDropdownChange}
                                color='secondary'
                            >
                                <MenuItem value={10}>Ten</MenuItem>
                                <MenuItem value={20}>Twenty</MenuItem>
                                <MenuItem value={30}>Thirty</MenuItem>
                            </Select>
                            </FormControl>
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