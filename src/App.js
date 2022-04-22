import React from "react";
import "./styles.css";
import Card from "./Card";
import NavBar from "./NavBar";
import { Grid } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  gridContainer: {
    paddingLeft: "40px",
    paddingRight: "40px",
    paddingTop: "40px"
  }
});

const numCards = 1

export default function App() {
  const classes = useStyles();

  return (
    <><NavBar></NavBar>
    <Grid container spacing={4} className={classes.gridContainer} justify="center">
     {[...Array(numCards)].map((e, i) => {
        return (
          <Grid item xs={12} sm={6} md={4}>
            <Card />
          </Grid>
        )
      })
    }
    </Grid></>
  );
}
