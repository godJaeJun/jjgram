import Reactotron from 'reactotron-react-js';
import { reactotronRedux } from 'reactotron-redux';

Reactotron.configure({ name: "JJagram" })
    .use(reactotronRedux())
    .connect();

export default Reactotron;