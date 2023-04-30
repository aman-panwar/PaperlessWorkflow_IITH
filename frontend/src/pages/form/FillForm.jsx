// Component that renders the form based on template - APPLICANT
import { useContext, useState } from 'react';
import { FormContext } from '../../App';
import { Box, Button } from '@mui/material';
import useMediaQuery from '@mui/material/useMediaQuery';
import Date from './fields/Date';
import File from './fields/File';
import Check  from './fields/Check';
import Dropdown from './fields/Dropdown';
import Text from './fields/Text';

const FillForm = () => {

    const { formType, setFormType, fillFormInfo, setFillFormInfo } = useContext(FormContext);
    const isNonMobile = useMediaQuery("(min-width:600px)");
    const req_fields = fillFormInfo['level_data'][0]['req_fields'];

    const render_elements = () => {
        const elements = []
        for(let i=0; i < req_fields.length; i++)
        {
            let display_name = req_fields[i][0]
            let field = req_fields[i][1];
            let item = <></>;
            if (field === 'textbox')
                item = <Text label={display_name}/>
            else if ( field === 'date')
                item = <Date/>
            else if ( field === 'dropdown')
            {
                let options = req_fields[i][2];
                item = <Dropdown label={display_name} options={options}/>
            }
            else if ( field === 'file')
                item = <File label={display_name}/>
            else if ( field === 'checkbox')
                item = <Check label={display_name}/>
            
            elements.push(item);
        }
        return elements;
    }

    const [formData, setFormData] = useState(null);

    const handleFormSubmit = (event) => {
        console.log("Submitted Form!");
        setFillFormInfo(null);
        setFormType(null);

        // event.preventDefault();
        // const form = event.target;
        // const formData = new FormData(form);
        // const data = Object.fromEntries(formData.entries());
        // console.log(data);
    }

    return ( 
        <form onSubmit={handleFormSubmit}>
            <Box 
                display="grid" 
                gap="30px" 
                gridTemplateColumns="repeat(4, minmax(0, 1fr))"
                sx = {{
                    "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
                }}
            >
            {render_elements()}
            </Box>
            <Box display="flex" justifyContent="end" mt="20px">
                <Button type="submit" color="secondary" variant="contained" onClick={handleFormSubmit}>
                    Submit Form
                </Button>
            </Box>
        </form>

    )
}

export default FillForm;