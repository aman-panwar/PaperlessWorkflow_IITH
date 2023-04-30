import { FormControl } from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers';
import { useState } from 'react';

const Date = () => {

  const [date, setDate] = useState(null);
  const changeDate = (newDate) => {
    setDate(newDate);
    console.log(newDate.format('L'));
  }
  return (
    <FormControl>
      <DatePicker
        name='DOB'
        value={date}
        onChange={changeDate}
        color='secondary'
        sx={{ gridColumn: "span 1" }}
      />

    </FormControl>
  );
}

export default Date;
