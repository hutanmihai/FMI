import { Controller, useFormContext } from 'react-hook-form'
import TextFieldsContainer from '@/components/form-containers/text-fields-container'

import { Button } from '@mui/material'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'

export default function RHFTechnologiesFields() {
  const { control } = useFormContext()

  return (
    <Controller
      name="technologies"
      control={control}
      render={({ field, fieldState: { error } }) => (
        <>
          <Typography variant="h6" textAlign="center" sx={{ mt: 2 }}>
            Technologies
          </Typography>
          <TextFieldsContainer>
            {field.value.map((technology: string, index: number) => (
              <TextField
                key={index}
                fullWidth
                {...field}
                value={technology}
                onChange={(e) => {
                  const newTechnologies = [...field.value]
                  newTechnologies[index] = e.target.value
                  field.onChange(newTechnologies)
                }}
                error={!!error}
                helperText={error && 'All technologies must not be empty'}
              />
            ))}
          </TextFieldsContainer>
          <Button
            variant="contained"
            color="primary"
            onClick={() => field.onChange([...field.value, ''])} // Add an empty string to the array
          >
            Add Technology
          </Button>
        </>
      )}
    />
  )
}
