import * as React from 'react';
import { 
    CssBaseline,
    Grid,
    createTheme,
    ThemeProvider,
 } from '@mui/material';


const defaultTheme = createTheme();

function SideImage() {

  return (
        <Grid item xs={false} sm={4} md={7} sx={{
            backgroundImage: 'url(https://source.unsplash.com/random?wallpapers)',
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
  );
}

export default SideImage;