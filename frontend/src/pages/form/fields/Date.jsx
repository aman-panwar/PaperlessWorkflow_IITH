import { DatePicker } from '@mui/x-date-pickers';
import { useState } from 'react';

const Date = () => {

    const [date, setDate] = useState(null);
    const changeDate = (newDate) => {
        setDate(newDate);
    }
    return(
        <DatePicker
            value ={date}
            onChange={changeDate}
            color='secondary'
            sx ={{ gridColumn: "span 1" }} 
        />
    );
}

export default Date;