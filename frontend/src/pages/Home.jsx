import Header from "../components/Header";
import TableStudents from "../components/Tables/TableStudent";
import TableClassrooms from "../components/Tables/TableClassroom";
import TableSubjects from "../components/Tables/TableSubjects";
import { Box } from "@mui/material";

function Home() {
  return (
    <div>
      <Header />
      <TableStudents />
      <Box
        sx={{
          display: "flex",
          justifyContent: "space-between",
          marginTop: "1vh",
        }}
      >
        <TableClassrooms />
        <TableSubjects />
      </Box>
    </div>
  );
}

export default Home;
