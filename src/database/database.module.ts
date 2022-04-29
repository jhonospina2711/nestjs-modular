import { Module, Global } from '@nestjs/common';

const API_KEY_DATABASE = '123456';
const API_KEY_PROD = 'PRO123456';

@Global()
@Module({
  providers: [
    {
      provide: 'API_KEY',
      useValue:
        process.env.NODE_ENV === 'prod' ? API_KEY_PROD : API_KEY_DATABASE,
    },
  ],
  exports: ['API_KEY'],
})
export class DatabaseModule {}
