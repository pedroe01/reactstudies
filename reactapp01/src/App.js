import Sobre from './Sobre';
import Teste from './Teste';
import Header from './Header';
import TesteApi from './TesteApi';
import ConsumeFlaskApi from './ConsumeFlaskApi'
import { Routes, Route, Link } from 'react-router-dom';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Link to='/sobre'>Sobre</Link> <br></br>
        <Link to='/teste'>Teste</Link> <br></br>
        <Link to='/header'>Header</Link> <br></br>
        <Link to='/apirequest'>Request API</Link> <br></br>
        <Link to='/flaskapi'>Request Flask API</Link> <br></br>
      </header>
      <main>
        <Routes>
            <Route path='/sobre' element={<Sobre/>}/>
            <Route path='/teste' element={<Teste/>}/>
            <Route path='/header' element={<Header/>}/>
            <Route path='/apirequest' element={<TesteApi/>}/>
            <Route path='/flaskapi' element={<ConsumeFlaskApi/>}/>
        </Routes>
    </main>
    </div>
  );
}

export default App;
